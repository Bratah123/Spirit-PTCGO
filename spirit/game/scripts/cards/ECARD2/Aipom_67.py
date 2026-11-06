from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, snipe_attack
from spirit.game.card_effects.ecard import skedaddle


card = PokemonCardDef(
    guid="8533a5d7-415c-57fd-aaad-77bd5193eed0",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Stretch Tail",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_or_nothing(then=snipe_attack(10)),
        ),
        Attack(
            title="Skedaddle",
            game_text="Return Aipom and all basic Energy cards attached to it to your hand. If you have no Benched Pok\u00e9mon, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=skedaddle,
        ),
    ],
)
