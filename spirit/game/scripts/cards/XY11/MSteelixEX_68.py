from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="740b73d8-0099-5c77-bcba-555ebf26d14c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSteelixEX.Name",
    display_name="M Steelix-EX",
    searchable_by=["M Steelix-EX", "MEGA", "EX", "MSteelixEX"],
    subtypes=["MEGA", "EX"],
    collector_number=68,
    set_code="XY11",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.METAL, PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SteelixEX.Name",
    family_id=208,
    abilities=[
        Attack(
            title="Canyon Axe",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=spread_damage(10, also_base=True),
        ),
    ],
)