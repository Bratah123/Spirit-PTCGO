from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import circular_steps, thick_fat_vs_types

card = PokemonCardDef(
    guid="1854c9aa-2669-5bec-8fa0-0117a2b1b3b8",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name",
    display_name="Grumpig",
    searchable_by=["Grumpig", "Stage 1", "Grumpig"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    family_id=325,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to Grumpig by attacks from Fire Pok\u00e9mon and Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=thick_fat_vs_types(30, PokemonTypes.FIRE, PokemonTypes.WATER),
            effect=None,
        ),
        Attack(
            title="Circular Steps",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play (both yours and your opponent's), excluding Grumpig.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
                        effect=circular_steps(10),
        ),
    ],
)