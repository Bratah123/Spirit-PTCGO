from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import psychic_shield_ex, cursed_glare_passive, safeguard_vs_ex_passive

card = PokemonCardDef(
    guid="ee7d4238-df65-59ef-aee7-305d4d98010e",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    display_name="Dusclops",
    searchable_by=["Dusclops", "Stage 1", "Dusclops"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Cursed Glare",
            game_text="As long as Dusclops is your Active Pok\u00e9mon, your opponent can't attach any Special Energy cards (except for Darkness and Metal Energy cards) from his or her hand to his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=cursed_glare_passive(),
            effect=None,
        ),
        Attack(
            title="Will-o'-the-wisp",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Psychic Shield",
            game_text="Prevent all effects of attacks, including damage, done to Dusclops by your opponent's Pok\u00e9mon-ex during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=psychic_shield_ex(),
        ),
    ],
)