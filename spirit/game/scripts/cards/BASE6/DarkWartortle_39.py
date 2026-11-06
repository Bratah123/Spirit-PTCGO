from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import mirror_shell


card = PokemonCardDef(
    guid="b3f3785d-3d70-516c-af57-6bad952e8784",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWartortle.Name",
    display_name="Dark Wartortle",
    searchable_by=["Dark Wartortle", "Stage 1", "DarkWartortle"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Doubleslap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Mirror Shell",
            game_text="If an attack does damage to Dark Wartortle during your opponent's next turn (even if Dark Wartortle is Knocked Out), Dark Wartortle does an equal amount of damage to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=mirror_shell,
        ),
    ],
)
