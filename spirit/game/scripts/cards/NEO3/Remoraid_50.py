from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, snipe_attack


card = PokemonCardDef(
    guid="95891e44-42a8-5932-bf88-ad7ad40692c5",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic", "Remoraid"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Sharpshooting",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.WATER: 1},
            effect=flip_or_nothing(then=snipe_attack(20, pool='any', apply_modifiers=False)),
        ),
    ],
)
