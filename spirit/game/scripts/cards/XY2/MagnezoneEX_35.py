from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="b57ccc0f-3d1c-5aa9-a472-7b486cb9b733",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneEX.Name",
    display_name="Magnezone-EX",
    searchable_by=["Magnezone-EX", "Basic", "EX", "MagnezoneEX"],
    subtypes=["Basic", "EX"],
    collector_number=35,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=462,
    abilities=[
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Dual Bullet",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            effect=snipe_attack(50, pool='any', count=2),
        ),
    ],
)