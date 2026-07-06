from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="076a309d-0e9a-53fd-9eb3-d515aa4a3f95",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianDecidueye.Name",
    display_name="Hisuian Decidueye",
    searchable_by=["Hisuian Decidueye", "Stage 2", "HisuianDecidueye"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Piercing Claw",
            game_text="This attack does 30 damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Direct Arrow",
            game_text="This attack does 80 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)