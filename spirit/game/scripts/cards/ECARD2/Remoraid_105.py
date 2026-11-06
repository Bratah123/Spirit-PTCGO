from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="2374a660-23a3-5e85-aebd-2e5c10308a56",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic", "Remoraid"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Splatter",
            game_text="Choose 1 of your opponent's Pok\u00e9mon is play. This attack does 10 damage to that Pok\u00e9mon. Don't apply Weakness or Resistance for this attack.",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(10, pool="any", apply_modifiers=False),
        ),
    ],
)
