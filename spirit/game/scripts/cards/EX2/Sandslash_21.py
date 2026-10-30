from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, spread_damage


card = PokemonCardDef(
    guid="48250881-9e69-56be-bf78-2e2036ab7f11",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1", "Sandslash"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Attack(
            title="Sand Swirl",
            game_text="Does 20 damage to each Defending Pok\u00e9mon. The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=condition_attack(no_retreat=True, damage=20),
        ),
        Attack(
            title="Earthquake",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
    ],
)
