from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import plasma, selfdestruct_attack


card = PokemonCardDef(
    guid="4538f30b-70ad-56d4-87eb-6eb4ccf8bbc9",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Plasma",
            game_text="If there are any Lightning Energy card in your discard pile, flip a coin. If heads, attach 1 of them to Electrode.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=plasma,
        ),
        Attack(
            title="Selfdestruct",
            game_text="This attack does 20 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Electrode does 100 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=selfdestruct_attack(bench_damage=20, self_damage=100),
        ),
    ],
)
