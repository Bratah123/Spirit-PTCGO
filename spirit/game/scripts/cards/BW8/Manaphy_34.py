from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="7d90b453-bc4c-53a4-8d97-d84ddccc3a46",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Final Wish",
            game_text="When this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Seafaring",
            game_text="Flip 3 coins. For each heads, attach a Water Energy card from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)