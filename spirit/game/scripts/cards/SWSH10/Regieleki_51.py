from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import electromagnetic_sonar, targeted_bolt

card = PokemonCardDef(
    guid="2c774fc4-f4cc-5f1f-9da9-8c79c816b295",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regieleki.Name",
    display_name="Regieleki",
    searchable_by=["Regieleki", "Basic", "Regieleki"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=894,
    abilities=[
        Attack(
            title="Electromagnetic Sonar",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=electromagnetic_sonar,
        ),
        Attack(
            title="Targeted Bolt",
            game_text="Discard 2 Lightning Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=targeted_bolt,
        ),
    ],
)
