from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import cat_punch


card = PokemonCardDef(
    guid="2cbb3780-687f-5e0a-a3bf-6c456c5eaaf4",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Cat Punch",
            game_text="Flip a coin. If heads, this attack does 20 damage. If tails and if your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=cat_punch,
        ),
    ],
)
