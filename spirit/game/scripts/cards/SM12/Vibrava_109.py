from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import obnoxious_whirring_passive

card = PokemonCardDef(
    guid="7420fffc-12a7-5ce3-a3fe-579476a115cb",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava",
    searchable_by=["Vibrava", "Stage 1", "Vibrava"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Obnoxious Whirring",
            game_text="Whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=obnoxious_whirring_passive,
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)