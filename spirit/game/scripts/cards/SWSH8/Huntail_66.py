from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df99ed28-b66c-52ac-a494-ed6652d9ce6d",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1", "Fusion Strike", "Huntail"],
    subtypes=["Stage 1", "Fusion Strike"],
    collector_number=66,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Ability(
            title="Single Strike Jammer",
            game_text="Your opponent's Single Strike Pok\u00e9mon's attacks cost Colorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Cavernous Chomp",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)