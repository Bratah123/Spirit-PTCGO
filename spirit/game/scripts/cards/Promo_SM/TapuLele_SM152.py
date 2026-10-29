from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    charmed_charm,
)

card = PokemonCardDef(
    guid="c9ec63b8-9a6d-5f19-948f-f572ddd7032e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name",
    display_name="Tapu Lele",
    searchable_by=["Tapu Lele", "Basic", "TapuLele"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=786,
    abilities=[
        Ability(
            title="Charmed Charm",
            game_text="Whenever you attach a Pok\u00e9mon Tool card that has \"Fairy Charm\" in its name from your hand to this Pok\u00e9mon during your turn, you may leave your opponent's Active Pok\u00e9mon Confused.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=charmed_charm,
            trigger=Triggers.ON_TOOL_ATTACHED,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)