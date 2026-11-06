from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play


card = PokemonCardDef(
    guid="3434508b-4a64-5040-95bd-90aa6f384355",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee", "Basic", "Combee"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=415,
    abilities=[
        Attack(
            title="Sting Missile",
            game_text="Shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=remove_self_from_play('deck'),
        ),
    ],
)