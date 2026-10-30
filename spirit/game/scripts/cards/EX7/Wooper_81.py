from spirit.game.card_effects.ex import saturation_on_water_attach
"""STUB: effect not implemented — do not guess mechanics.
Wooper (EX7 #81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=saturation_on_water_attach(1),
    guid="2fe3a3b4-62aa-546a-a204-a9c9987f4cd5",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic", "Wooper"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=194,
    abilities=[
        Ability(
            title="Saturation",
            game_text="When you attach a Water Energy card from your hand to Wooper, remove all Special Conditions and 1 damage counter from Wooper.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)