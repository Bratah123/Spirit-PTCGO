from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.sm7 import (
    steelworks,
)


card = PokemonCardDef(
    guid="acad9cb7-a5d7-5c8a-800e-53148f171664",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic", "Heatran"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=485,
    abilities=[
        Attack(
            title="Steelworks",
            game_text="Look at the top 4 cards of your deck and attach any number of Metal Energy cards you find there to 1 of your Pok\u00e9mon. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=steelworks,
        ),
        Attack(
            title="Steel Tackle",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=recoil_attack(30),
        ),
    ],
)