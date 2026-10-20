from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.session.passives import Passive, carrier_pokemon


async def _giga_power(ctx):
    """80; you may do 40 more damage. If you do, 20 damage to itself."""
    if await ctx.ask_yes_no("Do 40 more damage (this Pokémon does 20 damage to itself)?"):
        await recoil_attack(20, damage=120)(ctx)
    else:
        await ctx.deal_damage()


class _DoubleType(Passive):
    """As long as this Pokemon is in play, it is Psychic and Fighting type."""
    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        return [PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value]


card = PokemonCardDef(
    guid="919ae753-fcb6-5965-b628-3221c3def5b8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        ancient_trait('θ Stop'),
        Ability(
            title="Double Type",
            game_text="As long as this Pok\u00e9mon is in play, it is Psychic and Fighting type.",
            passive=_DoubleType(),
        ),
        Attack(
            title="Superpower",
            game_text="You may do 40 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="+",
            effect=_giga_power,
        ),
    ],
)