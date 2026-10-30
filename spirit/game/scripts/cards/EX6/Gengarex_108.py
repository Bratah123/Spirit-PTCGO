from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import poltergeist, prize_count

card = PokemonCardDef(
    guid="0e291b32-ea17-5662-9a1a-52daca8faf04",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengarex.Name",
    display_name="Gengar ex",
    searchable_by=["Gengar ex", "Stage 2", "ex", "Gengarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=108,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Look at your opponent's hand. This attack does 40 damage plus 10 more damage for each Trainer card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=poltergeist(40, 10),
        ),
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards left than your opponent, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=prize_count(60, 60),
        ),
    ],
)