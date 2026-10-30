from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack

card = PokemonCardDef(
    guid="3999a695-0983-5587-8bdc-6f7e8506d52b",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    display_name="Spoink",
    searchable_by=["Spoink", "Basic", "Spoink"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=325,
    abilities=[
        Attack(
            title="Bounce",
            game_text="After your attack, you may switch Spoink with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=switch_self_attack(optional=True),
        ),
    ],
)