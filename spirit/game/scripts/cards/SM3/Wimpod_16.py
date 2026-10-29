from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import WimpOutPassive

card = PokemonCardDef(
    guid="1fbf863b-a548-5f10-8842-9db1e4b33afc",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=767,
    abilities=[
        Ability(
            title="Wimp Out",
            game_text="During your first turn, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=WimpOutPassive(),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
