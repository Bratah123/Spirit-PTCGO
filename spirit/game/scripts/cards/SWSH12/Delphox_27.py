from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ba6ad51-dee9-5ae8-9411-399283a51c82",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Flare Parade",
            game_text="This attack does 60 damage for each Serena card in your discard pile.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Crush",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)