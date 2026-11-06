from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import fling, fling_condition


card = PokemonCardDef(
    guid="fe7b00e0-bc80-576c-9f87-b18a41247fe2",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMachamp.Name",
    display_name="Dark Machamp",
    searchable_by=["Dark Machamp", "Stage 2", "DarkMachamp"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMachoke.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
        Attack(
            title="Fling",
            game_text="Your opponent shuffles his or her Active Pok\u00e9mon and all cards attached to it into his or her deck. This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            effect=fling,
            condition=fling_condition,
        ),
    ],
)
