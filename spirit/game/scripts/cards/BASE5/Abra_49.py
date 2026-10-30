from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import remove_self_from_play


card = PokemonCardDef(
    guid="71616308-3e9a-5ddf-9cd6-74bbb9497861",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra", "Basic", "Abra"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Attack(
            title="Vanish",
            game_text="Shuffle Abra into your deck. (Discard all cards attached to Abra.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=remove_self_from_play("deck", with_attachments="discard"),
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
