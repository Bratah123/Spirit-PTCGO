from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb521319-ab64-512c-8567-6ee94f382ff6",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundVMAX.Name",
    display_name="Boltund VMAX",
    searchable_by=["Boltund VMAX", "VMAX", "BoltundVMAX"],
    subtypes=["VMAX"],
    collector_number=104,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    family_id=836,
    abilities=[
        Attack(
            title="Bolt Storm",
            game_text="This attack does 30 more damage for each Lightning Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Max Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't use Max Bolt.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=unimplemented,
        ),
    ],
)