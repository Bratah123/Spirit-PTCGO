from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1a7d9e3-2fee-55de-89f5-4d5fdd9a5c7a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    display_name="Inteleon V",
    searchable_by=["Inteleon V", "Basic", "V", "Rapid Strike", "InteleonV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=78,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=818,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Aqua Bullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=snipe_attack(20, also_base=True),
        ),
    ],
)