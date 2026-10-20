from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="249b996d-6c96-56ef-a97a-a22db6b03c9a",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    display_name="Tirtouga",
    searchable_by=["Tirtouga", "Restored", "Tirtouga"],
    subtypes=["Restored"],
    collector_number=25,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.RESTORED,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CoverFossil.Name",
    family_id=564,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)