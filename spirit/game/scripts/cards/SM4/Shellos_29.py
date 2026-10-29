from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="eae264f6-2014-5cf9-8148-444a11cb1f21",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    display_name="Shellos",
    searchable_by=["Shellos", "Basic", "Shellos"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=422,
    abilities=[
        Attack(
            title="Regeneration",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=heal_attack(30),
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)