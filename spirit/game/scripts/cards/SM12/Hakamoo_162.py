from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import fighters_roar_passive

card = PokemonCardDef(
    guid="78f6eef0-1817-562c-8bb3-03eb508e1757",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    display_name="Hakamo-o",
    searchable_by=["Hakamo-o", "Stage 1", "Hakamoo"],
    subtypes=["Stage 1"],
    collector_number=162,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    family_id=782,
    abilities=[
        Ability(
            title="Fighter's Roar",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-GX or Pok\u00e9mon-EX, this Pok\u00e9mon can evolve during the turn you play it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=fighters_roar_passive,
        ),
        Attack(
            title="Dragonslice",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)