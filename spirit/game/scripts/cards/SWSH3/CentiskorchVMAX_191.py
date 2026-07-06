from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e67a2398-6c80-523d-a2ad-86279b03dc6e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchVMAX.Name",
    display_name="Centiskorch VMAX",
    searchable_by=["Centiskorch VMAX", "VMAX", "CentiskorchVMAX"],
    subtypes=["VMAX"],
    collector_number=191,
    set_code="SWSH3",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    family_id=851,
    abilities=[
        Attack(
            title="G-Max Centiferno",
            game_text="This attack does 40 more damage for each Fire Energy attached to this Pok\u00e9mon. If you did any damage with this attack, you may attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)