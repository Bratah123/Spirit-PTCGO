from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import chain_lightning


card = PokemonCardDef(
    guid="d88de063-5287-5b93-8245-67f89eaefeee",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Chain Lightning",
            game_text="If the Defending Pok\u00e9mon isn't Colorless, this attack does 10 damage to each Benched Pok\u00e9mon of the same type as the Defending Pok\u00e9mon (including your own). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=20,
            effect=chain_lightning,
        ),
    ],
)
