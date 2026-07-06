from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98be6da3-5ced-5f5f-bd10-bfd86bc35794",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Cauterize",
            game_text="If your opponent's Active Pok\u00e9mon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)