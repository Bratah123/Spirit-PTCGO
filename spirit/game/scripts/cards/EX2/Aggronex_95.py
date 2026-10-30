from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage, spread_damage


card = PokemonCardDef(
    guid="73d8fa2b-25f4-5d88-80bd-1db5c60a4ce5",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggronex.Name",
    display_name="Aggron ex",
    searchable_by=["Aggron ex", "Stage 2", "ex", "Aggronex"],
    subtypes=["Stage 2", "ex"],
    collector_number=95,
    set_code="EX2",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon has any damage counters on it, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=bonus_if(has_damage(), 30),
        ),
        Attack(
            title="Metal Surge",
            game_text="Does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=spread_damage(20, also_base=True),
        ),
    ],
)
