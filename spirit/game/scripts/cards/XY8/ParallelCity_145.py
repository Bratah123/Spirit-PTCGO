from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.session.passives import Passive, effective_pokemon_types


# stadium entity_id -> player whose Bench is capped at 3 (the other player's
# Grass/Fire/Water attacks do 20 less).
_LIMITED = {}


async def parallel_city_facing(ctx):
    """Choose which way this card faces before you play it."""
    pick = await ctx.choose("Parallel City", ["Limit opponent's Bench to 3", "Limit your Bench to 3"],
                            use_panel=False)
    _LIMITED[ctx.source.entity_id] = ctx.player_id if pick == 1 else ctx.opponent_id


class _ParallelCity(Passive):
    def _limited(self, carrier):
        return _LIMITED.get(carrier.entity_id)

    def bench_capacity(self, player_id, carrier):
        return 3 if self._limited(carrier) == player_id else None

    def modify_damage_dealt(self, calc, carrier):
        limited = self._limited(carrier)
        att = calc.attacker
        if limited is None or att is None or not calc.is_attack or att.owning_player_id == limited:
            return
        types = effective_pokemon_types(calc.board, att)
        if any(t in types for t in (PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
                                    PokemonTypes.GRASS.value, PokemonTypes.FIRE.value, PokemonTypes.WATER.value)):
            calc.amount = max(0, calc.amount - 20)


card = StadiumCardDef(
    guid="77d73cc0-02bd-5f76-af1c-a81dfe223324",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParallelCity.Name",
    display_name="Parallel City",
    searchable_by=["Parallel City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=145,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=_ParallelCity(),
    abilities=[
        Ability(
            title="Parallel City",
            game_text="Choose which way this card faces before you play it.",
            trigger=Triggers.ON_PLAY,
            effect=parallel_city_facing,
        ),
    ]
)
