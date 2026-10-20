from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.session.passives import Passive, effective_pokemon_types


# stadium entity_id -> player whose Metal Pokemon take 10 less (the other
# player's Darkness Pokemon do 10 more).
_METAL_SIDE = {}


async def reverse_valley_facing(ctx):
    """Choose which way this card faces before you play it."""
    pick = await ctx.choose("Reverse Valley", ["My Metal Pokémon take 10 less", "My Darkness Pokémon do 10 more"],
                            use_panel=False)
    _METAL_SIDE[ctx.source.entity_id] = ctx.player_id if pick == 0 else ctx.opponent_id


def _has_type(board, pokemon, t):
    types = effective_pokemon_types(board, pokemon)
    return t in types or t.value in types


class _ReverseValley(Passive):
    def modify_damage_dealt(self, calc, carrier):
        metal = _METAL_SIDE.get(carrier.entity_id)
        att = calc.attacker
        if (metal is None or att is None or not calc.is_attack or not calc.is_opposing
                or not calc.to_active or att.owning_player_id == metal):
            return
        if _has_type(calc.board, att, PokemonTypes.DARKNESS):
            calc.amount += 10

    def modify_damage_taken(self, calc, carrier):
        metal = _METAL_SIDE.get(carrier.entity_id)
        if (metal is None or not calc.is_attack or not calc.is_opposing
                or calc.target.owning_player_id != metal):
            return
        if _has_type(calc.board, calc.target, PokemonTypes.METAL):
            calc.amount = max(0, calc.amount - 10)


card = StadiumCardDef(
    guid="4243938d-79db-5a5e-889c-d38432a88f37",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReverseValley.Name",
    display_name="Reverse Valley",
    searchable_by=["Reverse Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=110,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=_ReverseValley(),
    abilities=[
        Ability(
            title="Reverse Valley",
            game_text="Choose which way this card faces before you play it.",
            trigger=Triggers.ON_PLAY,
            effect=reverse_valley_facing,
        ),
    ]
)
