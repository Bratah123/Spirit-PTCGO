from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="b14b27a5-f7c2-512f-a347-9c5e50864bbb",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    display_name="Gurdurr",
    searchable_by=["Gurdurr", "Stage 1", "Gurdurr"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Steel Swing",
            game_text="Flip 2 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=60),
        ),
    ],
)