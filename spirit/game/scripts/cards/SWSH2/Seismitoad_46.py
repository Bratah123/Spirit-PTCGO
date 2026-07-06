from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28bbd7eb-498c-5bf1-899a-381dfaba3e88",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Split Spiral Punch",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Resonance",
            game_text="If your opponent's Active Pok\u00e9mon is Confused, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)