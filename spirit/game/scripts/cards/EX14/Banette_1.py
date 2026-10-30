from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import night_murmurs_confuse_basic, safeguard_vs_ex_passive

card = PokemonCardDef(
    guid="7b9f37c1-1166-518d-8476-5af364fc6974",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to Banette by your opponent's Pok\u00e9mon-ex.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=safeguard_vs_ex_passive(),
            effect=None,
        ),
        Attack(
            title="Night Murmurs",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, that Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
                        effect=night_murmurs_confuse_basic(),
        ),
    ],
)