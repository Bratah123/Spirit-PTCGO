from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm3 import synchronoise


card = PokemonCardDef(
    guid="01cff739-aee1-5c8e-8ac3-afdd146a1091",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name",
    display_name="Bruxish",
    searchable_by=["Bruxish", "Basic", "Bruxish"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=779,
    abilities=[
        Attack(
            title="Gnash Teeth",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Synchronoise",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that shares a type with your opponent's Active Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=synchronoise,
        ),
    ],
)
