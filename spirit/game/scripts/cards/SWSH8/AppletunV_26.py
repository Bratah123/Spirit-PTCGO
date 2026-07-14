from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="527eb679-687b-5260-b684-11c4a4316bb7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AppletunV.Name",
    display_name="Appletun V",
    searchable_by=["Appletun V", "Basic", "V", "AppletunV"],
    subtypes=["Basic", "V"],
    collector_number=26,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=842,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Sweet Impact",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=heal_attack(30),
        ),
    ],
)