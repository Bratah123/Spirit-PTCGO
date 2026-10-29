from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play

card = PokemonCardDef(
    guid="caf1a7a7-b02e-58a1-b667-90a5a142ca1c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=767,
    abilities=[
        Attack(
            title="Scamper Away",
            game_text="Shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=remove_self_from_play("deck"),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
