from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import ExtremeSpeedPassive, fire_blow


card = PokemonCardDef(
    guid="6e5179e6-3f7c-5057-abcc-a19fd5b868f1",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=152,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Extreme Speed",
            game_text="You pay Colorless less to retreat Arcanine for each Energy attached to it.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=ExtremeSpeedPassive(),
        ),
        Attack(
            title="Fire Blow",
            game_text="You may discard any number of Fire Energy cards attached to Arcanine when you use this attack. If you do, flip a number of coins equal to the number of Fire Energy cards you discarded. This attack does 30 damage plus 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=fire_blow,
        ),
    ],
)
