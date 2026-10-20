from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="a3cb8176-6b89-5be4-ab0b-3a003ee9cfa5",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    display_name="Loudred",
    searchable_by=["Loudred", "Stage 1", "Loudred"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 30, base=30),
        ),
    ],
)