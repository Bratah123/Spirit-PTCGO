from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import no_weakness_or_resistance, selfdestruct_attack


card = PokemonCardDef(
    guid="b402961d-25ee-55a9-966e-7b2bd24d475e",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=82,
    abilities=[
        Attack(
            title="Sonicboom",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=no_weakness_or_resistance,
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 20 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Magneton does 100 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=100,
            effect=selfdestruct_attack(bench_damage=20, self_damage=100),
        ),
    ],
)
