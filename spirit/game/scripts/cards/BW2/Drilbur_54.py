from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_own_next_turn_boost


async def hone_claws(ctx):
    """No damage. During your next turn, this Pokémon's attacks do 30 more."""
    await apply_own_next_turn_boost(ctx, 30)


card = PokemonCardDef(
    guid="627abe51-2952-5290-8474-cb995a2092fc",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=529,
    abilities=[
        Attack(
            title="Hone Claws",
            game_text="During your next turn, each of this Pok\u00e9mon's attacks does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hone_claws,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
