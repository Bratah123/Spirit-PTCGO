from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents

card = PokemonCardDef(
    guid="3ff45355-32a4-56c1-b266-de35b57d80df",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceV.Name",
    display_name="Salamence V",
    searchable_by=["Salamence V", "Basic", "V", "SalamenceV"],
    subtypes=["Basic", "V"],
    collector_number=185,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=373,
    abilities=[
        Attack(
            title="Swoop Across",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=damage_all_opponents(30),
        ),
        Attack(
            title="Heavy Storm",
            cost={PokemonTypes.COLORLESS: 4},
            damage=160,
        ),
    ],
)