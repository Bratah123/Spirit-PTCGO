from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e5fe8ac4-a08f-5117-a9d2-255f162a4596",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Freefloating",
            game_text="If this Pok\u00e9mon has no Energy attached to it, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)