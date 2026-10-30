from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import burn_away_heal_on_ko, drag_off_optional


card = PokemonCardDef(
    guid="684e3479-13ad-516b-8000-d33c341955fa",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blazikenex.Name",
    display_name="Blaziken ex",
    searchable_by=["Blaziken ex", "Stage 2", "ex", "Blazikenex"],
    subtypes=["Stage 2", "ex"],
    collector_number=90,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=drag_off_optional(),
        ),
        Attack(
            title="Burn Away",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon. If that Pok\u00e9mon is Knocked Out by this attack, Blaziken ex does damage to itself equal to the attack's damage minus the remaining HP of the Defending Pok\u00e9mon. This attack's damage isn't by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
                        effect=burn_away_heal_on_ko(),
        ),
    ],
)