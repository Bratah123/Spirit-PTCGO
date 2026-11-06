from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import elemental_blast, elemental_blast_condition


card = PokemonCardDef(
    guid="7abadedb-5330-5ea2-ae16-d81c462a0e7b",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Elemental Blast",
            game_text="Discard a Fire Energy card, a Water Energy card, and a Lightning Energy card attached to Lugia in order to use this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=90,
            condition=elemental_blast_condition,
            effect=elemental_blast,
        ),
    ],
)
