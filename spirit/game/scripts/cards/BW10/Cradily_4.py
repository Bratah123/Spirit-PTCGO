from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="631adac5-0299-5470-80a8-28a34d1af971",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 1", "Cradily"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Lifesplosion",
            game_text="For each Energy attached to this Pok\u00e9mon, search your deck for a Stage 2 Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=heal_attack(20),
        ),
    ],
)