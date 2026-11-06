from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ecard import armor_up


card = PokemonCardDef(
    guid="4ae42081-2705-5af6-8bc8-2ff662cd063a",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkForretress.Name",
    display_name="Dark Forretress",
    searchable_by=["Dark Forretress", "Stage 1", "DarkForretress"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Armor Up",
            game_text="Until the end of your next turn, if Dark Forretress would be Knocked Out by damage from an attack, flip a coin. If heads, Dark Forretress is not Knocked Out and its remaining HP become 10 instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=armor_up,
        ),
        Attack(
            title="Explosion",
            game_text="Dark Forretress does 60 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            effect=recoil_attack(60),
        ),
    ],
)
