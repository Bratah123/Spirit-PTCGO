from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="35ed6de8-51a1-513f-a6c9-02bd2f6d37ac",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    display_name="Quilladin",
    searchable_by=["Quilladin", "Stage 1", "Quilladin"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=heal_attack(10),
        ),
        Attack(
            title="Needle Arm",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)